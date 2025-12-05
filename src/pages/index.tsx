import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import HomepageFeatures from '../components/HomepageFeatures'; // Ensure this import is present
import HomepageCTA from '../components/HomepageCTA'; // Import new CTA component

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--dark', styles.heroBanner)}> {/* Changed hero--primary to hero--dark for black/purple background */}
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/course-overview"> {/* Link to the new course-overview page */}
            Get Started
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`} /* Updated title for better SEO */
      description="Learn Physical AI & Humanoid Robotics with our comprehensive course." /* Updated description */
    >
      <HomepageHeader />
      <section className={styles.sectionPadding}>
        <div className="container">
          <div className="row">
            <div className="col col--12">
              <Heading as="h2">Why Physical AI & Humanoid Robotics?</Heading>
              <p>
                The convergence of Artificial Intelligence with physical robotics, especially humanoid forms, represents the next frontier in technological evolution. This course delves into the intricate challenges and groundbreaking solutions in designing, programming, and deploying robots that can interact intelligently and physically with the human world. From advanced perception and cognitive reasoning to delicate manipulation and robust locomotion, understanding this field is crucial for anyone looking to contribute to a future where intelligent machines seamlessly integrate into our daily lives.
              </p>
              <p>
                As industries worldwide embrace automation and intelligent systems, the demand for experts in Physical AI and Humanoid Robotics is skyrocketing. This curriculum provides the foundational knowledge and practical skills needed to thrive in this rapidly expanding domain, empowering you to build the intelligent, human-centric robots of tomorrow.
              </p>
            </div>
          </div>
        </div>
      </section>
      <main>
        <HomepageFeatures />
      </main>
      <HomepageCTA /> {/* New CTA component */}
    </Layout>
  );
}
