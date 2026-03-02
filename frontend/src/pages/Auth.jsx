import { useState } from 'react'
import { api } from '../lib/api'

export default function Auth(){
  const [form,setForm]=useState({email:'',password:'',role:'researcher'})
  const [token,setToken]=useState('')
  const submit = async (path) => { const {data}=await api.post(path,form); setToken(data.access_token) }
  return <div className='p-8 space-y-3 max-w-lg'>
    {['email','password','role'].map(k=><input key={k} className='w-full p-2 bg-slate-900 border border-slate-700 rounded' placeholder={k} value={form[k]} onChange={e=>setForm({...form,[k]:e.target.value})} />)}
    <div className='flex gap-2'><button className='card' onClick={()=>submit('/auth/signup')}>Signup</button><button className='card' onClick={()=>submit('/auth/login')}>Login</button></div>
    {token && <p className='break-all text-xs'>{token}</p>}
  </div>
}
