import ChartCard from '../components/ChartCard'

export default function RobustnessLab(){
  return <div className='p-8 grid lg:grid-cols-2 gap-4'>
    <div className='card space-y-2'>{['Gaussian noise','Blur','Brightness','Rotation','Scaling','Compression','Occlusion','FGSM/PGD'].map(x=><label key={x} className='block text-sm'>{x}<input type='range' className='w-full' /></label>)}</div>
    <ChartCard title='Robustness Degradation' data={[{x:[0,0.2,0.4,0.6,0.8],y:[0.9,0.84,0.72,0.61,0.4],type:'scatter'}]} layout={{height:360}} />
  </div>
}
