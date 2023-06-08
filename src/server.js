const mongo_uri = "mongodb+srv://hitman:zaeem123@cluster0.rmbcl.mongodb.net/?retryWrites=true&w=majority"

const { MongoClient } = require('mongodb');


// uploading data to database

const client = new MongoClient(mongo_uri);

async function setData(binance, data) {
    try {
        const collection = client.db("binance").collection('data');

        // Check if data already exists against the symbol


    } catch (e) {
        console.error(e);
    } finally {
        await client.close();
    }
}