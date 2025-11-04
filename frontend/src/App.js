import React, { useState } from 'react';

function App() {
  const [mood, setMood] = useState('');
  const [recipes, setRecipes] = useState([]);
  const [error, setError] = useState(null);

  const moods = ['happy', 'sad', 'energetic', 'calm'];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setRecipes([]);
    try {
      const response = await fetch('/api/mood', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ mood }),
      });
      if (!response.ok) {
        const errData = await response.json();
        setError(errData.error || 'Unknown error');
        return;
      }
      const data = await response.json();
      setRecipes(data.recipes);
    } catch (err) {
      setError('Failed to fetch recipes');
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: 'auto', padding: '1rem' }}>
      <h1>Mood-Based Recipe Recommendation</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="mood">Select your mood:</label>
        <select id="mood" value={mood} onChange={(e) => setMood(e.target.value)} required>
          <option value="">--Choose mood--</option>
          {moods.map((m) => (
            <option key={m} value={m}>
              {m.charAt(0).toUpperCase() + m.slice(1)}
            </option>
          ))}
        </select>
        <button type="submit" style={{ marginLeft: '1rem' }}>Get Recipes</button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {recipes.length > 0 && (
        <div>
          <h2>Recommended Recipes</h2>
          <ul>
            {recipes.map((r) => (
              <li key={r.id}>{r.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
