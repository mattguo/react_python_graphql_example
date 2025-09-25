import type { FilmListQuery } from './__generated__/FilmListQuery.graphql';
import { graphql, useLazyLoadQuery } from 'react-relay';
import React from 'react';

const FilmList: React.FC = () => {
  const data = useLazyLoadQuery<FilmListQuery>(
    graphql`
      query FilmListQuery {
        allFilms {
          films {
            id
            title
            director
          }
        }
      }
    `,
    {}
  );

  return (
    <div>
      <h1>Star Wars Films</h1>
      {JSON.stringify(data)}
    </div>
  );
};

export default FilmList;
