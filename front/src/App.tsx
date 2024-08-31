import { useState } from 'react'
import './App.css'
import RecordForm, { Record } from './record-form/RecordForm'

function App() {
  const [records, setRecords] = useState([
    { id: "209af90d-f68d-4488-ae1e-31ce79cb8d39", title: "勉強の記録1", time: 1},
    { id: "f24ae960-8c4c-4c4d-834b-132abcea1579", title: "勉強の記録2", time: 3},
    { id: "cf7bd3cf-8716-46e5-be23-0d1584e6c6c2", title: "勉強の記録3", time: 5}
  ])
  const [totalTime, setTotalTime] = useState(records.reduce((sum, record) => sum + record.time, 0))

  const listItems = records.map(record => <li key={record.id}>{record.title}: {record.time} 時間</li>);

  function addRecord(record: Record) {
    setRecords([...records, record])
    setTotalTime(totalTime + record.time)
  }

  return (
    <>
      <RecordForm
        onSubmit={(record) => addRecord(record)}>
      </RecordForm>
      <div>
        <ul>{listItems}</ul>
      </div>
      <div>
        合計時間: {totalTime}
      </div>
    </>
  )
}

export default App
