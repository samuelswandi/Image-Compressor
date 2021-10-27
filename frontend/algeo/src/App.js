import './App.css';

function App() {
  return (
    <div className="App">
      {/* HEADER */}
      <div className="header">
        <p>This image optimizer uses a smart combination of the best optimization and lossy compression algorithms to shrink JPEG, GIF and PNG images to the minimum possible size while keeping the required level of quality.</p>

      </div>

      {/* CONTAINER FOR FILE */}
      <div className="file-container">
        <button onClick = "">Upload File</button>
        <div className="input-file-container">
          <p>Drop your file here</p>
        </div>

      </div>

      {/* FOOTER */}
      <div className="footer">
      <p>Tubes Algeo 2</p>
      <p>©  Kelompok 22 | IF20</p>
      </div>
    </div>
  );
}

export default App;
