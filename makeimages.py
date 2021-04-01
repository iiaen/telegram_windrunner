from bokeh.io import export_png, export_svgs
from bokeh.models import ColumnDataSource, DataTable, TableColumn
# from bokeh.plotting import show

def save_df_as_image(df, path):
    source = ColumnDataSource(df)
    df_columns = df.columns.values
    columns_for_table=[]
    for column in df_columns:
        columns_for_table.append(TableColumn(field=column, title=column))
    
    height=30*len(df) + 5
    data_table = DataTable(source=source, columns=columns_for_table, 
                           autosize_mode="fit_columns", height=height,
                           index_position=None)
    #show(data_table)
    export_png(data_table, filename = path)