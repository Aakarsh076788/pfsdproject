import { useState } from 'react'
import ChartCard from '../components/ChartCard'

export default function TrainingLab(){
  const [assistant, setAssistant] = useState('')
  const loss=[1.2,0.9,0.7,0.5], acc=[0.42,0.61,0.74,0.86]
  const handleVoice = () => {
    const rec = new window.webkitSpeechRecognition();
    rec.onresult=(e)=>setAssistant(e.results[0][0].transcript)
    rec.start()
  }
  return <div className='p-8 space-y-4'>
    <div className='grid md:grid-cols-3 gap-3'>
      {['ResNet','EfficientNet','MobileNet','DenseNet'].map(a=><button key={a} className='card'>{a}</button>)}
    </div>
    <div className='grid md:grid-cols-2 gap-4'>
      <ChartCard title='Loss vs Epoch' data={[{x:[1,2,3,4],y:loss,type:'scatter'}]} layout={{height:300}} />
      <ChartCard title='Accuracy vs Epoch' data={[{x:[1,2,3,4],y:acc,type:'scatter'}]} layout={{height:300}} />
    </div>
    <div className='card'><h3>Conversational + Voice Assistant</h3><input className='w-full p-2 bg-slate-950 border border-slate-700 mt-2' placeholder='e.g. start training with lr 3e-4' value={assistant} onChange={e=>setAssistant(e.target.value)} /><button className='mt-2 px-3 py-2 bg-emerald-600 rounded' onClick={handleVoice}>Voice Command</button></div>
  </div>
}
