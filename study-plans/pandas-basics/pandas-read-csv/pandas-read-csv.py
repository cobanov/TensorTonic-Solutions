import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    
    df = pd.DataFrame.from_dict(data)
    return {
        "data": df.to_dict(orient="list"),
        "shape": list(df.shape),
        "columns": df.columns.to_list()
    }