const mongoose = require("mongoose");
const mongo_uri = "mongodb+srv://hitman:zaeem123@cluster0.rmbcl.mongodb.net/?retryWrites=true&w=majority";

function connection() {
    const connectionParams = {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    };
    try {
        mongoose.connect(mongo_uri, connectionParams);
        console.log("Connected to database ");
    }
    catch (error) {
        console.log(error);
        console.log("Could not connect to the database!");
    }
}

// Push Data to Database
function PushData(binance_api, data) {
    const Data = mongoose.model("Data", {
        _id: binance_api,
        data: data,
    });

    const newData = new Data({ _id: binance_api, data: data });
    newData.save((err) => {
        if (err) {
            console.log(err);
            return false;
            // Handle the error as per your requirements
        } else {
            console.log("Data Pushed");
            return true;
            // Handle the case when the registration is successful
        }
    });
}


// login
function Login(binance_api, password) {
    // Assuming you have a "User" model defined with a "binance_api" and "password" field
    const User = mongoose.model("User", {
        binance_api: String,
        password: String,
    });

    User.findOne({ binance_api: binance_api }, (err, user) => {
        if (err) {
            console.log(err);
            // Handle the error as per your requirements
        } else if (!user) {
            console.log("User not found");
            // Handle the case when the user is not found
        } else if (user.password !== password) {
            console.log("Incorrect password");
            // Handle the case when the password is incorrect
        } else {
            console.log("Login successful");
            // Handle the case when the login is successful
        }
    });
}

// register
function Register(binance_api, password) {
    // Assuming you have a "User" model defined with a "binance_api" and "password" field
    const User = mongoose.model("User", {
        binance_api: String,
        password: String,
    });

    const newUser = new User({ binance_api, password });
    newUser.save((err) => {
        if (err) {
            console.log(err);
            // Handle the error as per your requirements
        } else {
            console.log("Registration successful");
            // Handle the case when the registration is successful
        }
    });
}