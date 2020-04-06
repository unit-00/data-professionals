import io

class Pipeline:
    def __init__(self, engine):
        self.engine = engine
        self.conn = engine.raw_connection()
        self.c = self.conn.cursor()
        
    def add_table(self, df, table_name):
        with self.engine.connect() as connection:
            df.head(0).to_sql(table_name, self.engine, if_exists='replace', index=False)
            output = io.StringIO()
            df.to_csv(output, sep='\t', header=False, index=False)
            output.seek(0)
            self.c.copy_from(output, table_name, null='')
            self.conn.commit()
    