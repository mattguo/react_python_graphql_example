import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import FilmList from './FilmList';
import { Container, Group, Button, Image, Stack } from '@mantine/core';

function App() {
  const [count, setCount] = useState(0);

  return (
    <Stack gap="xl">
      <FilmList />
      <Container size="lg">
        <Group justify="center" align="center" gap="md" wrap="nowrap">
          <Image
            src={reactLogo}
            alt="React logo"
            w={50}
            h={50}
            style={{ cursor: 'help' }}
          />
          <Button
            onClick={() => setCount(count => count + 1)}
            size="md"
            variant="filled"
          >
            count is {count}
          </Button>
        </Group>
      </Container>
    </Stack>
  );
}

export default App;
