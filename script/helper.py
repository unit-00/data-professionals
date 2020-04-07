import numpy as np
import scipy.stats as stats
import seaborn as sns

def plot_quant(ax, df, xlabel='', ylabel='', title='', **options):
    sns.kdeplot(df, **options)
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title)
    

def plot_cat(ax, x, df, xlabel='', ylabel='', title='', **options):
    sns.countplot(x=x, data=df, ax=ax , **options)
    
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title)
    
def plot_kde(ax, nl, pl, al, xlabel='', ylabel='', title='', **options):
    sns.kdeplot(nl, label='Not Looking', shade=True)
    sns.kdeplot(pl, label='Passively Looking', shade=True)
    sns.kdeplot(al, label='Actively Looking', shade=True)
    
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title)
    

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
    table = np.array([n, p, a])
    chi, p, dof, expected = stats.chi2_contingency(table)

    return p