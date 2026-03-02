export default function Explainability(){
  return <div className='p-8 grid md:grid-cols-3 gap-3'>{['Grad-CAM','Saliency','Activation Map'].map(x=><div key={x} className='card'><h3>{x}</h3><div className='h-40 bg-gradient-to-br from-emerald-700 to-violet-700 rounded mt-2' /></div>)}</div>
}
