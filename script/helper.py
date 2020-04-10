import numpy as np
import scipy.stats as stats
import seaborn as sns

def plot_quant(ax, df, xlabel='', ylabel='', title='', **options):
    sns.kdeplot(df, **options)
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title, fontsize=15)
    

def plot_cat(ax, x, df, xlabel='', ylabel='', title='', **options):
    sns.countplot(x=x, data=df, ax=ax , **options)
    
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title, fontsize=15)
    
def plot_kde(ax, nl, pl=[], al=[], nl_label='Not Looking', pl_label='Passively Looking', al_label='Actively Looking', xlabel='', ylabel='', title='', **options):
    sns.kdeplot(nl, label=nl_label, shade=True)
    sns.kdeplot(pl, label=pl_label, shade=True)
    sns.kdeplot(al, label=al_label, shade=True)
    
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title, fontsize=15)
    
def plot_hypo(ax, s1, s2, xlabel='', ylabel='', title='', **options):
    test, p = stats.ttest_ind(s1, s2, equal_var=False)
    df = welch_satterhwaithe_df(s1, s2)
    
    
    x = np.linspace(-4.5, 4.5, 250)
    t = stats.t(df)
    
    sns.lineplot(x, t.pdf(x), **options)

    ax.vlines(x=t.ppf(0.975), ymin=0, ymax=0.5, color='#000000', linestyle='--', label='alpha', zorder=3)

    ax.vlines(x=test, ymin=0, ymax=0.5, color='r', linestyle='--', label='p value', zorder=3)

    ax.fill_between(x, t.pdf(x), where=(x >= test), color="red", alpha=0.25)
    
                
    
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title, fontsize=15)
    
    ax.legend(fontsize='xx-large', loc='upper left')
    
    
def plot_power(ax, s1, s2, xlabel='', ylabel='', title='', **options):

    x = np.linspace(-8, 8, 250)
    se = se_welch(s1, s2)
    df = welch_satterhwaithe_df(s1, s2)
    
    null = stats.t(df=df)
    alt = stats.t(loc=(s1.mean() - s2.mean())/se, df=df)

    sns.lineplot(x, null.pdf(x), label='null')
    sns.lineplot(x, alt.pdf(x), label='alt')
    ax.vlines(x=null.ppf(0.975), ymin=0, ymax=0.5, color='#000000', linestyle='--', label='alpha', zorder=1)

    ax.fill_between(x, alt.pdf(x), where=(x >= null.ppf(0.97)), color="red", alpha=0.25)



    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title, fontsize=15)

    ax.legend(fontsize='xx-large', loc='upper left')

def samps_ttest(nl, pl, al):
    t1, p1 = stats.ttest_ind(nl, pl, equal_var=False)
    t2, p2 = stats.ttest_ind(pl, al, equal_var=False)
    t3, p3 = stats.ttest_ind(nl, al, equal_var=False)
    
    return (('nl, pl', p1), ('pl, al', p2), ('nl, al', p3))

def samps_mwu(nl, pl, al):
    t1, p1 = stats.mannwhitneyu(nl, pl)
    t2, p2 = stats.mannwhitneyu(pl, al)
    t3, p3 = stats.mannwhitneyu(nl, al)
    
    return (('nl, pl', p1), ('pl, al', p2), ('nl, al', p3))

def samps_chi2(nl, pl, al):
    n = nl.value_counts().sort_index()
    p = pl.value_counts().sort_index()
    a = al.value_counts().sort_index()
    
    n_index = n.index
    p_index = p.index
    a_index = a.index
    
    all_index = set(n_index) | set(p_index) | set(a_index)

    new_n = []
    new_p = []
    new_a = []
    
    for i in all_index:
        
        if i not in n_index:
            new_n.append(0)
        else:
            new_n.append(n[i])
            
        if i not in p_index:
            new_p.append(0)
        else:
            new_p.append(p[i])
            
        if i not in a_index:
            new_a.append(0)
        else:
            new_a.append(a[i])
        
        
    table = np.array([new_n, new_p, new_a])
    chi, p, dof, expected = stats.chi2_contingency(table)

    return p

def outliers_removed(series):
    q3 = series.quantile(.75)
    q1 = series.quantile(.25)
    
    iqr = q3 - q1
    mask = ((series < (q3 + 1.5 * iqr)) & (series > (q1 - 1.5 * iqr)))
    
    return series[mask]
                    
def se_welch(n1, n2):
    s1 = n1.var()/(n1.size)
    s2 = n2.var()/(n2.size)

    return np.sqrt(s1 + s2)
    
    

def power_calc(n1, n2, alpha=.05):
    se = se_welch(n1, n2)

    null = stats.norm(0, se)
    alt = stats.norm(n1.mean() - n2.mean(), se)

    cv_left = null.ppf((alpha/2))
    cv_right = null.ppf(1 - (alpha/2))
    
    power = alt.cdf(cv_left) + 1 - alt.cdf(cv_right)
    
    return round(power, 2)

def power_analysis(n1, n2, n3):
    p1 = power_calc(n1, n2)
    p2 = power_calc(n2, n3)
    p3 = power_calc(n1, n3)
    
    print(f'Not & Passive: {p1:2.2f}')
    print(f'Passive & Active: {p2:2.2f}')
    print(f'Not & Active: {p3:2.2f}')

def welch_satterhwaithe_df(sample_1, sample_2):
    ss1 = len(sample_1)
    ss2 = len(sample_2)
    df = (
        ((np.var(sample_1)/ss1 + np.var(sample_2)/ss2)**(2.0)) / 
        ((np.var(sample_1)/ss1)**(2.0)/(ss1 - 1) + (np.var(sample_2)/ss2)**(2.0)/(ss2 - 1))
    )
    return df

def calc_ab(data):
    mu = data.mean()
    a = 1 + (data.size/2)
    
    ssd = ((data - mu) ** 2).sum()
    b = 1 + ssd/2
    
    return a, b