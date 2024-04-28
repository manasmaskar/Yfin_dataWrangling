
# from raw_to_tabular import convertDF
import pandas as pd



# Assuming you already have a DataFrame named `stock_data_df` containing data for all companies


def create_combined_dataframe(stock_data_df):
    """
    Combines individual company data into a single DataFrame with company names.

    Args:
    stock_data_df (pandas.DataFrame): DataFrame containing individual company data.

    Returns:
    pandas.DataFrame: Combined DataFrame with company names.
    """
    # Create a list of company names without '_data' suffix and convert them to lowercase
    company_names = ['aapl', 'msft', 'googl', 'jpm', 'bac', 'wfc', 'jnj', 'pfe', 'mrk', 'xom', 'cvx', 'cop', 'vz', 'meta', 't']

    # Initialize an empty list to store DataFrames
    dfs = []

    # Iterate over company names and create DataFrames for each company
    for company in company_names:
        # Create a new DataFrame for the company
        df = pd.DataFrame(stock_data_df[company + '_data'])
        # Add a new column 'Company' with the lowercase company name
        df.insert(0, 'Company', company)
        # Append the DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames together
    final_df = pd.concat(dfs, ignore_index=True)

    # Dictionary mapping ticker symbols to full company names
    ticker_to_full = {
        'aapl': 'Apple',
        'msft': 'Microsoft',
        'googl': 'Google',
        'jpm': 'JPMorgan Chase & Co',
        'bac': 'Bank of America Corp',
        'wfc': 'Wells Fargo',
        'jnj': 'Johnson & Johnson',
        'pfe': 'Pfizer',
        'mrk': 'Merck',
        'xom': 'Exxon Mobil Corp',
        'cvx': 'Chevron Corp',
        'cop': 'ConocoPhillips',
        'vz': 'Verizon',
        'meta': 'Facebook',
        't': 'T'
    }

    # Rename the company names in the 'Company' column
    final_df['Company'] = final_df['Company'].map(ticker_to_full)

    return final_df