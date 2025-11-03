import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Cat Meow Translator heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/Cat Meow Translator/i);
  expect(headingElement).toBeInTheDocument();
});
