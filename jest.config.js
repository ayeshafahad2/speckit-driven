// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/setupTests.js'], // Optional setup file
  testPathIgnorePatterns: ['/node_modules/', '/.docusaurus/', '/build/'],
  transform: {
    '^.+\.(js|jsx|ts|tsx)$': '<rootDir>/node_modules/babel-jest',
    '^.+\.css$': '<rootDir>/config/jest/cssTransform.js', // Handle CSS imports
    '^(?!.*\.(js|jsx|ts|tsx|css|json)$)': '<rootDir>/config/jest/fileTransform.js', // Handle other static assets
  },
  transformIgnorePatterns: [
    'node_modules/(?!(.*docusaurus.*)|(react-native-safe-area-context))',
  ],
  moduleNameMapper: {
    '^@site/(.*)$': '<rootDir>/$1',
    '^@generated/(.*)$': '<rootDir>/.docusaurus/generated/$1',
    '^@docusaurus/(.*)$': '<rootDir>/node_modules/@docusaurus/$1',
    '^~/(.*)$': '<rootDir>/src/$1', // Map ~ to src folder
    '\.(css|less|sass|scss)$': 'identity-obj-proxy', // Mock CSS modules
  },
};
