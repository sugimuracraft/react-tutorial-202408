import { useEffect, useState } from 'react'
import { Settings } from '../settings'
import { StudyRecord } from './Types'

interface FormProps {
  initialData?: StudyRecord
  onSubmit: (record: StudyRecord) => void
  onCancel: () => void
}

function StudyRecordForm({ initialData, onSubmit, onCancel }: FormProps) {
  const [title, setTitle] = useState('')
  const [time, setTime] = useState<number | ''>('')
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState('')

  useEffect(() => {
    if (!initialData) {
      return
    }
    setTitle(initialData.title)
    setTime(initialData.time)
  }, [initialData])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // validate forms.
    if (title.trim() === '' || time === '') {
      return
    }

    setLoading(true)

    let response$
    if (!initialData) {
      // creation
      response$ = fetch(
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
    }
    else {
      // updation
      response$ = fetch(
        `${Settings.APIEndPoint}/study-records/${initialData.id}`,
        {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            title: title,
            time: time,
          })
        },
      )
    }
    response$
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok.')
      }
      return response.json()
    })
    .then((data: StudyRecord) => {
      setMessage('Study record created successfully!')
      // clear forms.
      setTitle('')
      setTime('')
      setLoading(false)
      onSubmit(data)
    })
    .catch(err => {
      setMessage(err.message)
      setLoading(false)
    })
  }

  const handleCancel = (e: React.FormEvent) => {
    e.preventDefault()
    setTitle('')
    setTime('')
    onCancel()
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
          <button type="submit">{!initialData ? "Create" : "Update"}</button>
          <button type="button" onClick={handleCancel}>Cancel</button>
        </div>
      </form>
      {loading && <p>Sending...</p>}
    </>
  )
}

export default StudyRecordForm
