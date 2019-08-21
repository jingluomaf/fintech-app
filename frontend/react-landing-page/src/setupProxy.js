const proxy = require("http-proxy-middleware");

module.exports = function(app) {
  app.use(
    "/jupyter",
    proxy({
      target: "http://localhost:8888/",
      logLevel: "debug",
      secure: false,
      changeOrigin: true
    })
  );
};
