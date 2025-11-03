import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const catTranslations = [
  "Feed me, human!",
  "I require more chin scratches.",
  "The red dot is my mortal enemy.",
  "I will nap here, and here, and also there.",
  "Are you going to finish that?",
  "My food bowl is half-empty!",
  "I demand your attention!",
  "Pet me... but only for a second.",
  "I'm plotting world domination from this sunbeam.",
  "The dog is looking at me funny again."
];

function App() {
  const [translation, setTranslation] = useState('');

  const translateMeow = () => {
    const randomIndex = Math.floor(Math.random() * catTranslations.length);
    setTranslation(catTranslations[randomIndex]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cat Meow Translator</h1>
        <img src="/cat.jpg" className="img-fluid rounded-circle cat-image" alt="A cute cat" />
        <button className="btn btn-primary btn-lg mt-4" onClick={translateMeow}>
          Translate Meow!
        </button>
        {translation && (
          <div className="alert alert-success mt-4" role="alert">
            <h4 className="alert-heading">The cat says:</h4>
            <p>{translation}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;