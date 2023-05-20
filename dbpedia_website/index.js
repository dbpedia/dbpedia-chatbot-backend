const express = require('express');
const app = express();
app.use(express.static(__dirname + "/public/"));
app.listen(process.env.PORT || "4000", function() {
    console.log("server running on port 4000");
})