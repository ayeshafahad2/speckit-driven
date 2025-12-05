import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';
import Heading from '@theme/Heading';

export default function HomepageCTA(): JSX.Element {
  return (
    <section className={clsx(styles.homepageCta)}>
      <div className="container">
        <div className="row">
          <div className="col col--12 text--center">
            <Heading as="h2" className={styles.ctaHeading}>
              Ready to Master the Future of Robotics?
            </Heading>
            <p className={styles.ctaDescription}>
              Join our comprehensive course and become an expert in Physical AI and Humanoid Robotics. Start building the intelligent machines that will shape tomorrow's world.
            </p>
            <div className={styles.buttons}>
              <Link
                className="button button--secondary button--lg"
                to="/docs/course-overview">
                View Course Curriculum
              </Link>
              <Link
                className="button button--primary button--lg"
                to="#"> {/* Placeholder for enrollment link */}
                Enroll Now
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}