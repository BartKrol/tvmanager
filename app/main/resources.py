from flask.ext import restful
from tvrage import api
from datetime import date


series_list = ['Supernatural', 'Gotham', 'Flash', 'Suits', 'Arrow']


def get_next_episode(series):
    for episode in series.current_season.values():
        if (episode.airdate is not None) and (episode.airdate >= date.today()):
            return {'season': episode.season, 'code': episode.number,
                    'title': episode.title, 'airdate': episode.airdate.isoformat()}


def get_previous_episode(series):
    episode = series.latest_episode
    return {'season': episode.season, 'code': episode.number,
            'title': episode.title, 'airdate': episode.airdate.isoformat()}


class Episodes(restful.Resource):
    def get(self):
        series_info = []
        for series_name in series_list:
            series = api.Show(series_name)

            previous_episode = get_previous_episode(series)
            next_episode = get_next_episode(series)
            series_info.append(dict(previous=previous_episode, next=next_episode, name=series_name))

        return series_info
