import { Settings } from '../settings'
import { StudyRecord } from './Types'

interface ItemProps {
  data: StudyRecord
  onChange: () => void
}

function StudyRecordItem({ data, onChange }: ItemProps) {
  const handleDelete = (e: React.FormEvent) => {
    e.preventDefault()

    fetch(
      `${Settings.APIEndPoint}/study-records/${data.id}`,
      {
        method: 'DELETE',
      },
    )
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok.')
      }
      return response.json()
    })
    .then(() => onChange())
    .catch(error => console.error('Error fetching study records:', error))
  }

  return (
    <li key={data.id}>
      <h2>{data.title}</h2>
      <p>{data.time} 時間</p>
      <button onClick={handleDelete}>削除</button>
    </li>
  )
}

export default StudyRecordItem
