import io
class SqlPipeline:
    
    def __init__(self, engine):
        self.engine = engine
        self.conn = self.engine.raw_connection()
        self.c = self.conn.cursor()
        
    def add_table(self, df, table_name):
        
        df.head(0).to_sql(table_name, self.engine, if_exists='replace', index=False)
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        self.c.copy_from(output, table_name, null='')
        self.conn.commit()
        

    def close(self):
        self.conn.close()
        self.engine.dispose()

# Unused for now

class MongoPipeline:
    
    def __init__(self, client, db, coll):
        self.client = client
        self.db = client[db]
        self.collection = self.db[coll]
        
    def add_one(self, doc):
        self.collection.insert_one(doc)
    
    def close(self):
        self.client.close()
        