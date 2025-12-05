import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  img: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Module 1: The Robotic Nervous System (ROS 2)',
    img: require('@site/static/img/one.png').default, // Placeholder SVG
    description: (
      <>
        Master ROS 2 fundamentals: nodes, topics, services, and Python integration for robust robot control. Learn to define humanoid structures with URDF.
      </>
    ),
  },
  {
    title: 'Module 2: The Digital Twin (Gazebo & Unity)',
    img: require('@site/static/img/two.png').default, // Placeholder SVG
    description: (
      <>
        Dive into realistic physics simulations with Gazebo and high-fidelity rendering/HRI in Unity. Simulate LiDAR, depth cameras, and IMUs for virtual robots.
      </>
    ),
  },
  {
    title: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
    img: require('@site/static/img/three.png').default, // Placeholder SVG
    description: (
      <>
        Explore advanced AI perception and training with NVIDIA Isaac Sim for synthetic data, Isaac ROS for accelerated VSLAM, and Nav2 for humanoid path planning.
      </>
    ),
  },
  {
    title: 'Module 4: Vision-Language-Action (VLA)',
 img: require('@site/static/img/four.png').default, // Placeholder SVG
    description: (
      <>
        Bridge LLMs and robotics: implement voice commands with OpenAI Whisper, cognitive planning, and complete a Capstone Project on autonomous humanoid interaction.
      </>
    ),
  },
];

function Feature({title, img, description}: FeatureItem) {
  return (
    <div className={clsx('col col--6')}> {/* Changed to col--6 for 2 columns per row */}
      <div className="text--center">
        <img className={styles.featureSvg} alt={title} src={img} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
