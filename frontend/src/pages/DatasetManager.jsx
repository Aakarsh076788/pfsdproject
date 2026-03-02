import ChartCard from '../components/ChartCard'

export default function DatasetManager(){
  const data=[{x:['healthy','blight','rust'],y:[120,80,30],type:'bar',marker:{color:'#34d399'}}]
  return <div className='p-8 grid lg:grid-cols-2 gap-4'>
    <div className='card'><h2 className='font-bold mb-2'>Dataset Upload & Preview</h2><input type='file' multiple className='block' /><p className='mt-2 text-sm'>Imbalance detected for class rust. Suggested augmentation: mixup + oversampling.</p></div>
    <ChartCard title='Class Distribution' data={data} layout={{height:320}} />
  </div>
}
