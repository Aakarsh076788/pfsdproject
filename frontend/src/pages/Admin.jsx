export default function Admin(){
  return <div className='p-8 grid md:grid-cols-3 gap-3'>
    {['System monitoring','User management','Resource usage'].map(x=><div key={x} className='card'>{x}</div>)}
  </div>
}
