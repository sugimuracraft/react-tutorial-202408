import { v4 as uuidv4 } from 'uuid'
import { useState } from 'react'

export type Record = {
  id: string;
  title: string;
  time: number;
};

interface RecordFormProps {
  onSubmit: (record: Record) => void;
}

function RecordForm({ onSubmit }: RecordFormProps) {
  const [title, setTitle] = useState('');
  const [time, setTime] = useState<number | ''>('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // validate forms.
    if (title.trim() === '' || time === '') {
      return;
    }

    onSubmit({
      id: uuidv4(),
      title: title,
      time: Number(time)
    })

    // clear forms.
    setTitle('');
    setTime('');
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            学習内容
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            ></input>
          </label>
        </div>
        <div>
          <label>
            学習時間
            <input
              type="number"
              value={time}
              onChange={(e) => setTime(Number(e.target.value))}
              required
            ></input>
          </label>
        </div>
        <div>
          <button type="submit">
            保存
          </button>
        </div>
      </form>
    </>
  )
}

export default RecordForm
