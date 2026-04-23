import { useEffect, useState } from 'react'
import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || ''

export default function App() {
  const [prompt, setPrompt] = useState('Design a high-performance sports car with futuristic styling.')
  const [result, setResult] = useState(null)
  const [reports, setReports] = useState([])
  const [loading, setLoading] = useState(false)

  const loadReports = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/reports`)
      setReports(response.data)
    } catch (err) {
      console.error('Failed to load reports:', err)
    }
  }

  useEffect(() => {
    loadReports()
  }, [])

  const handleGenerate = async () => {
    setLoading(true)
    try {
      const response = await axios.post(`${API_BASE_URL}/api/generate-report`, { prompt })
      setResult(response.data)
      await loadReports()
    } catch (err) {
      console.error('Generation failed:', err)
      alert('Error: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ fontFamily: 'Segoe UI, sans-serif', padding: 24, maxWidth: 1100, margin: '0 auto' }}>
      <header style={{ borderBottom: '2px solid #111', paddingBottom: 14, marginBottom: 24 }}>
        <h1>AutoMind Vehicle Generator</h1>
        <p>Generate one concept vehicle and its specifications.</p>
      </header>

      <section style={{ marginBottom: 28, padding: 16, backgroundColor: '#f6f6f6', borderRadius: 8 }}>
        <h2>Input</h2>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          rows={4}
          style={{ width: '100%', padding: 10, marginBottom: 12 }}
          placeholder='Describe the vehicle you want...'
        />
        <button
          onClick={handleGenerate}
          disabled={loading}
          style={{
            padding: '10px 20px',
            border: 'none',
            borderRadius: 6,
            backgroundColor: loading ? '#888' : '#111',
            color: '#fff',
            cursor: loading ? 'not-allowed' : 'pointer',
          }}
        >
          {loading ? 'Generating...' : 'Generate Vehicle'}
        </button>
      </section>

      {result && (
        <section style={{ marginBottom: 28, padding: 16, backgroundColor: '#fff', border: '1px solid #ddd', borderRadius: 8 }}>
          <h2>{result.vehicle_name}</h2>

          {result.image_url && (
            <div style={{ marginBottom: 16 }}>
              <img
                src={result.image_url.startsWith('http') ? result.image_url : `${API_BASE_URL}${result.image_url}`}
                alt={result.vehicle_name}
                style={{ width: '100%', maxHeight: 520, objectFit: 'cover', borderRadius: 8 }}
              />
            </div>
          )}

          {!result.image_url && result.image_error && (
            <div style={{ marginBottom: 16, padding: 10, borderRadius: 6, backgroundColor: '#fff3cd', color: '#7a5d00' }}>
              Image generation failed: {result.image_error}
            </div>
          )}

          <h3>Specifications</h3>
          <ul>
            {(result.specifications || []).map((line, idx) => (
              <li key={idx}>{line}</li>
            ))}
          </ul>

          <h3>Details</h3>
          <p style={{ lineHeight: 1.6 }}>{result.vehicle_details}</p>
        </section>
      )}

      <section>
        <h2>Recent Vehicles ({reports.length})</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: 14 }}>
          {reports.map((report) => (
            <div key={report.report_id} style={{ border: '1px solid #ddd', borderRadius: 8, padding: 14 }}>
              <h4>{report.title}</h4>
              <p style={{ color: '#555' }}>{report.snippet}</p>
              <small>{new Date(report.created_at).toLocaleString()}</small>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}
