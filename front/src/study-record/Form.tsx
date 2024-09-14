import { useState } from 'react'
import { Settings } from '../settings'

export type StudyRecord = {
  id: string
  title: string
  time: number
};

interface FormProps {
  onSubmit: (record: StudyRecord) => void
}

function StudyRecordForm({ onSubmit }: FormProps) {
  const [title, setTitle] = useState('')
  const [time, setTime] = useState<number | ''>('')
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // validate forms.
    if (title.trim() === '' || time === '') {
      return
    }

    setLoading(true)

    fetch(
      `${Settings.APIEndPoint}/study-records`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: title,
          time: time,
        })
      },
    )
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok.')
      }
      return response.json()
    })
    .then((data: StudyRecord) => {
      setMessage('Study record created successfully!')
      // clear forms.
      setTitle('');
      setTime('');
      setLoading(false)
      onSubmit(data)
    })
    .catch(err => {
      setMessage(err.message)
      setLoading(false)
    })
  }

  return (
    <>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>学習内容</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          ></input>
        </div>
        <div>
          <label>学習時間</label>
          <input
            type="number"
            value={time}
            onChange={(e) => setTime(Number(e.target.value))}
            required
          ></input>
        </div>
        <div>
          <button type="submit">
            保存
          </button>
        </div>
      </form>
      {loading && <p>Sending...</p>}
    </>
  )
}

export default StudyRecordForm
