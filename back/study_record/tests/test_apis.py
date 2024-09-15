from pytest import fixture, mark


class TestStudyRecordCreate:
    @fixture
    def target(self):
        return "/study-records"

    def test_response_ok(self, target, client):
        from fastapi import status

        res = client.post(
            target,
            json={
                "title": "Title1",
                "time": 1,
            },
        )

        assert res.status_code == status.HTTP_200_OK

    @mark.parametrize(
        "title, time, description",
        [
            (None, "1", "title is None"),
            ("", "1", "title is empty"),
            ("Title1", None, "time is None"),
            ("Title1", "a", "title is not int 1"),
            ("Title1", "1.1", "title is not int 2"),
        ],
    )
    def test_validation_ng(self, target, client, title, time, description):
        from fastapi import status

        res = client.post(
            target,
            json={
                "title": title,
                "time": time,
            },
        )

        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, description


class TestStudyRecordList:
    @fixture
    def target(self):
        return "/study-records"

    def test_empty(self, target, client):
        """should be available as page 1, even if the number of data items is zero."""
        res = client.get(
            target,
        )

        actual = res.json()
        expected = {
            "total_count": 0,
            "total_time": 0,
            "study_records": [],
        }
        assert actual == expected

    def test_pagenation(self, target, client):
        """should be retrieved the target data.
        - test count param.
        - test page param.
        - test sort order.
        - test total_count.
        - test total_time.
        """
        from study_record.tests.factories import StudyRecordFactory

        StudyRecordFactory(time=1)
        StudyRecordFactory(title="title2", time=2)  # target data.
        StudyRecordFactory(time=4)
        StudyRecordFactory(time=8)

        res = client.get(
            target,
            params={
                "c": 1,
                "p": 2,
            },
        )
        res_json = res.json()

        actual = {
            "total_count": res_json["total_count"],
            "total_time": res_json["total_time"],
            "title": res_json["study_records"][0]["title"],
            "time": res_json["study_records"][0]["time"],
        }
        expected = {
            "total_count": 4,
            "total_time": 15,
            "title": "title2",
            "time": 2,
        }
        assert actual == expected


class TestStudyRecordRetrieve:
    @fixture
    def target(self):
        def _method(id: int):
            return f"/study-records/{id}"

        return _method

    def test_response_ok(self, target, client):
        from fastapi import status

        from study_record.tests.factories import StudyRecordFactory

        study_record = StudyRecordFactory()

        res = client.get(
            target(study_record.id),
        )

        assert res.status_code == status.HTTP_200_OK

    def test_not_found(self, target, client):
        from uuid import uuid4

        from fastapi import status

        res = client.get(
            target(str(uuid4())),  # dummy id.
        )

        assert res.status_code == status.HTTP_404_NOT_FOUND


class TestStudyRecordUpdate:
    @fixture
    def target(self):
        def _method(id: int):
            return f"/study-records/{id}"

        return _method

    def test_response_ok(self, target, session, client):
        from fastapi import status

        from study_record.tests.factories import StudyRecordFactory

        study_record = StudyRecordFactory(title="before update", time=1)

        res = client.put(
            target(study_record.id),
            json={
                "title": "Title1",
                "time": 2,
            },
        )
        study_record = StudyRecordFactory.refresh_from_db(study_record, session)

        actual = {
            "status_code": res.status_code,
            "title": study_record.title,  # how to refresh?
            "time": study_record.time,  # how to refresh?
        }
        expected = {
            "status_code": status.HTTP_200_OK,
            "title": "Title1",
            "time": 2,
        }
        assert actual == expected

    @mark.parametrize(
        "title, time, description",
        [
            (None, "1", "title is None"),
            ("", "1", "title is empty"),
            ("Title1", None, "time is None"),
            ("Title1", "a", "title is not int 1"),
            ("Title1", "1.1", "title is not int 2"),
        ],
    )
    def test_validation_ng(self, target, client, title, time, description):
        from fastapi import status

        from study_record.tests.factories import StudyRecordFactory

        study_record = StudyRecordFactory()

        res = client.put(
            target(study_record.id),
            json={
                "title": title,
                "time": time,
            },
        )

        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, description

    def test_not_found(self, target, client):
        from uuid import uuid4

        from fastapi import status

        res = client.put(
            target(str(uuid4())),  # dummy id.
            json={
                "title": "Title1",
                "time": 2,
            },
        )

        assert res.status_code == status.HTTP_404_NOT_FOUND


class TestStudyRecordDelete:
    @fixture
    def target(self):
        def _method(id: int):
            return f"/study-records/{id}"

        return _method

    def test_response_ok(self, target, session, client):
        from fastapi import status

        from study_record.tests.factories import StudyRecordFactory

        study_record = StudyRecordFactory(title="before update", time=1)

        res = client.delete(
            target(study_record.id),
        )
        study_record = StudyRecordFactory.refresh_from_db(study_record, session)

        actual = {
            "status_code": res.status_code,
            "study_record": study_record,
        }
        expected = {
            "status_code": status.HTTP_200_OK,
            "study_record": None,
        }
        assert actual == expected

    def test_not_found(self, target, client):
        from uuid import uuid4

        from fastapi import status

        res = client.delete(
            target(str(uuid4())),  # dummy id.
        )

        assert res.status_code == status.HTTP_404_NOT_FOUND
