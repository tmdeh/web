var path = require("path");

module.exports = {
    publicPath: './',
    //outputDir: path.resolve("../backend/public"),
    devServer: {
        proxy: {
            '^/api': {
                target: 'http://localhost:3000',
                changeOrigin: true
            }
        }
    }
}