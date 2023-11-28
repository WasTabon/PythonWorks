import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(file_name):
    df = pd.read_csv(file_name)
    df.drop_duplicates(inplace=True)
    cleaned_df = df.dropna().copy()
    return cleaned_df

def merge_data(df1, df2, key):
    return pd.merge(df1, df2, how='inner', on=key)

def get_statistics(df):
    return df.describe()

def get_unique_counts(df):
    return df.nunique()

def get_min_max_values(df):
    return df.min(), df.max()

def plot_loss_dynamics(df, x_col, y_col, x_label, y_label, title):
    plt.figure(figsize=(10, 5))
    plt.plot(df[x_col], df[y_col])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

# Load and clean data
equipment_df = load_and_clean_data('russia_losses_equipment.csv')
corrections_df = load_and_clean_data('russia_losses_equipment_correction.csv')
personnel_df = load_and_clean_data('russia_losses_personnel.csv')

# Merge data
merged_df = merge_data(equipment_df, corrections_df, 'date')

# Get statistics
equipment_stats = get_statistics(equipment_df)

# Get unique counts
unique_counts_equipment = get_unique_counts(equipment_df)

# Get min and max values
min_value_equip, max_value_equip = get_min_max_values(corrections_df)

# Plotting
plot_loss_dynamics(equipment_df, 'date', 'aircraft', 'Дата', 'Кількість втраченої техніки', 'Динаміка втрат літаків')