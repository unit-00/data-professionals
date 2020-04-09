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
    

def samps_ttest(nl, pl, al):
    t1, p1 = stats.ttest_ind(nl, pl)
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