import ChartCard from '../components/ChartCard'

export default function Comparison(){
  return <div className='p-8 space-y-4'>
    <ChartCard title='Model Ranking by RSI' data={[{x:['ResNet','EffNet','MobileNet','DenseNet'],y:[82,88,74,85],type:'bar'}]} layout={{height:320}} />
    <div className='card'>Calibration Analyzer, Uncertainty Estimation (MC Dropout), Cross-dataset generalization, Failure explorer, Bias detector, Drift monitor and deployment simulation are integrated via backend APIs.</div>
  </div>
}
