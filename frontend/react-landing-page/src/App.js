import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <iframe title="w3" src="http://test:9000" width="100%" />
      <iframe title="w3" src="http://test:8000" width="100%" />
      <iframe title="w3" src="http://test:8080" width="100%" />
      <iframe title="w3" src="http://test:8888" width="100%" />
      <iframe title="w3" src="http://test:9090" width="100%" />
    </div>
  );
}

export default App;
