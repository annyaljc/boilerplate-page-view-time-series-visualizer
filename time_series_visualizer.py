import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date',parse_dates=['date'])


lower=df['value'].quantile(0.025)
higher=df['value'].quantile(0.975)

# Clean data
df = df[(df['value']>lower)&(df['value']<higher)]

def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(18,6))
    sns.lineplot(x=df.index, y='value', data=df,color='red')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig=plt.gcf()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    monthly_avg = df.groupby(['year','month']).mean().reset_index()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    plt.figure(figsize=(10, 8))
    
    # Draw the bar plot
    sns.barplot(x='year', y='value', hue='month', data=monthly_avg, palette='tab10',hue_order=month_order)
    
    # Customize labels and title
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views by Month and Year')
    plt.legend(title='Months')

    fig=plt.gcf()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0],hue='year',palette='Set1')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order,hue='month',palette='coolwarm')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    axes[1].tick_params(axis='x', rotation=45)
    
    # Adjust layout
    plt.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
