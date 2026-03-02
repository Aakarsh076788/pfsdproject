import { motion } from 'framer-motion'

export default function Landing(){
  return <div className='p-8 space-y-6'>
    <motion.h1 initial={{opacity:0,y:20}} animate={{opacity:1,y:0}} className='text-4xl font-bold text-emerald-400'>AgroRobust AI</motion.h1>
    <p className='text-slate-300 max-w-4xl'>Scientific platform for CNN crop disease detection robustness, calibration, explainability, uncertainty, and deployment simulation under real-world shifts.</p>
    <div className='grid md:grid-cols-3 gap-4'>
      {['Train CNNs','Stress-test robustness','Generate research PDFs'].map((x)=><motion.div key={x} whileHover={{scale:1.03}} className='card'>{x}</motion.div>)}
    </div>
  </div>
}
