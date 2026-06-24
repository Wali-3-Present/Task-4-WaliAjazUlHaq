import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def initialize_visualization_pipeline():
    print("=" * 75)
    print("   DECODELABS DATA ANALYTICS INTERNSHIP: PROJECT 4 (VISUALIZATION)")
    print("=" * 75)
    
    csv_path = "data/Dataset for Data Analytics.xlsx - Sheet1.csv"
    output_dir = "outputs"
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: Dataset could not be located at '{csv_path}'")
        return
        
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure global styling context for crisp outputs
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 16
    })
    
    # Load and clean types
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    print("✔ Dataset parsed successfully. Generating descriptive visual plots...")
    
    # -------------------------------------------------------------
    # Plot 1: Pareto Product Performance (Bar Chart)
    # -------------------------------------------------------------
    plt.figure(figsize=(10, 6))
    prod_rev = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).reset_index()
    
    ax1 = sns.barplot(x='TotalPrice', y='Product', data=prod_rev, palette="viridis")
    plt.title("Revenue Contribution Vectors by Product Line", pad=15, weight='bold')
    plt.xlabel("Total Cumulative Revenue ($)")
    plt.ylabel("Product Classification")
    
    # Annotate bar weights directly onto presentation plane
    for p in ax1.patches:
        width = p.get_width()
        ax1.text(width + (width * 0.01), p.get_y() + p.get_height()/2 + 0.1, 
                 f"${width:,.2f}", ha="left", va="center", fontsize=9, weight='semibold')
                 
    plt.tight_layout()
    plt.savefig(f"{output_dir}/product_revenue.png", dpi=300)
    plt.close()
    print("📊 Plot 1 generated: 'outputs/product_revenue.png'")
    
    # -------------------------------------------------------------
    # Plot 2: Historical Revenue Vector Trajectory (Line Chart)
    # -------------------------------------------------------------
    plt.figure(figsize=(12, 6))
    df['YearMonth'] = df['Date'].dt.to_period('M')
    time_series = df.groupby('YearMonth')['TotalPrice'].sum().reset_index()
    time_series['YearMonth'] = time_series['YearMonth'].astype(str)
    
    sns.lineplot(x='YearMonth', y='TotalPrice', data=time_series, marker='o', color='#1a73e8', linewidth=2.5)
    plt.fill_between(time_series['YearMonth'], time_series['TotalPrice'], color='#1a73e8', alpha=0.1)
    
    plt.title("E-Commerce Gross Revenue Trajectory Over Time", pad=15, weight='bold')
    plt.xlabel("Timeline Period (Year-Month)")
    plt.ylabel("Gross Monthly Revenue ($)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/monthly_sales_trend.png", dpi=300)
    plt.close()
    print("📈 Plot 2 generated: 'outputs/monthly_sales_trend.png'")
    
    # -------------------------------------------------------------
    # Plot 3: Logistics Pipeline Share Breakdown (Pie Chart)
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 8))
    status_shares = df['OrderStatus'].value_counts()
    
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#f1c40f', '#95a5a6']
    plt.pie(status_shares, labels=status_shares.index, autopct='%1.1f%%', startangle=140, 
            colors=colors[:len(status_shares)], explode=[0.02] * len(status_shares),
            textprops={'fontsize': 11, 'weight': 'semibold'})
            
    plt.title("Logistics Allocation & Order Status Breakdown", pad=20, weight='bold')
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/order_status_distribution.png", dpi=300)
    plt.close()
    print("🍩 Plot 3 generated: 'outputs/order_status_distribution.png'")
    print("=" * 75)
    print("✨ Execution Complete! All visualization artifacts are saved in your '/outputs/' folder.")

if __name__ == "__main__":
    initialize_visualization_pipeline()