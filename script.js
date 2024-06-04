// Create a web API using express and JavaScript with routes for products and customers
// USe Ctrl + Enter for applying all the suggestions
const express = require('express');
const app = express();
app.path('/products', () => "products");
app.path('/customers', () => "customers");
app.listen(3000, () => console.log('Server is running on port 3000'));