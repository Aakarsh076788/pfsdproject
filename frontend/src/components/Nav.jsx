import { Link } from 'react-router-dom'

const links = [
  ['/', 'Landing'], ['/auth', 'Auth'], ['/datasets', 'Dataset Manager'], ['/training', 'Training Lab'], ['/robustness', 'Robustness Lab'], ['/explainability', 'Explainability'], ['/comparison', 'Model Compare'], ['/admin', 'Admin']
]

export default function Nav(){
  return <nav className='flex flex-wrap gap-3 p-4 border-b border-slate-800'>{links.map(([to,label])=><Link key={to} to={to} className='px-3 py-1 rounded bg-slate-800 hover:bg-emerald-700'>{label}</Link>)}</nav>
}
