const { MongoClient } = require('mongodb');

const url = "mongodb+srv://hitman:zaeem123@cluster0.rmbcl.mongodb.net/?retryWrites=true&w=majority"

async function connectToMongoDB() {
  try {
    // Connect to MongoDB
    const client = await MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true });

    // Access the database
    const db = client.db();

    // Perform database operations
    // ...

    // Close the connection
    client.close();
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
  }
}

connectToMongoDB();
