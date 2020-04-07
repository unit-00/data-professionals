def plot_quant(ax, df, xlabel='', ylabel='', title='', **options):
    ax.hist(df, **options)
    
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title)
    

def plot_cat(ax, df, xlabel='', ylabel='', title='', **options):
    x = df.index
    ax.bar(x, df, **options)
    
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_title(title)
    