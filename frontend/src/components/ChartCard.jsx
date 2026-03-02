import Plot from 'react-plotly.js'

export default function ChartCard({ title, data, layout }) {
  return <div className='card'><h3 className='mb-2 font-semibold'>{title}</h3><Plot data={data} layout={{paper_bgcolor:'#0f172a', plot_bgcolor:'#0f172a', font:{color:'#e2e8f0'}, ...layout}} style={{width:'100%'}} useResizeHandler /></div>
}
