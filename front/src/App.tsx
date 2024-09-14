import { useEffect, useState } from 'react';
import './App.css'
import { Settings } from './settings';
import StudyRecordForm from './study-record/Form'
import StudyRecordList from './study-record/List'


function App() {
  const [studyRecords, setStudyRecords] = useState({
    totalCount: 0,
    studyRecords: [],
  }); // リストの状態を管理

  // 初期表示で保存済みのリストを API から取得
  useEffect(() => {
    refreshList()
  }, [])

  function refreshList() {
    // APIから最新のStudyRecordを取得してリストを更新する
    fetch(`${Settings.APIEndPoint}/study-records`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok.')
        }
        return response.json()
      })
      .then(data => setStudyRecords({
        totalCount: data.total_count,
        studyRecords: data.study_records,
      }))
      .catch(error => console.error('Error fetching study records:', error))
  }

  return (
    <>
      <StudyRecordForm
        onSubmit={() => refreshList()} // Form送信後にリストをリフレッシュ
      />
      <StudyRecordList
        data={studyRecords}
        onChange={() => refreshList()}
      />
    </>
  )
}

export default App
