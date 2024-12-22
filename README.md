### Report on Docker Command Tasks and Project Setup

This report provides an overview of the Docker commands needed for specific operations, as well as a detailed explanation of how to set up and execute a project using Docker.

---

### 1. **Docker Commands**

#### Copy a Local Directory to a Container
To copy a local directory to a directory inside the container named `hello`:
```bash
docker cp /path/to/local/directory hello:/test/
```

#### Copy All `.log` Files from Container to Local Machine
To copy all `.log` files from the `test/` directory inside the `hello` container to the local `home/` directory:
```bash
docker cp hello:/test/*.log /path/to/local/home/
```

#### Get Docker Image Information and Save to a File
To get the image information and save it to a file named `i.json`:
```bash
docker inspect <image-name> > i.json
```

#### Show Only the IDs of All Containers
To show only the IDs of all containers:
```bash
docker ps -q
```

#### Show Only the IDs of All Images
To show only the IDs of all images:
```bash
docker images -q
```

#### Pull and Run the Hadoop Image
To pull the Hadoop image and run the container:
```bash
docker pull hadoop
docker run -d --name hadoop-container hadoop
```

#### Simple Dockerfile to Create an Image from Fedora with Python
Here is an example of a Dockerfile to create an image based on Fedora with Python:
```dockerfile
FROM fedora:latest

# Install Python
RUN dnf install -y python3

# Install necessary libraries
RUN dnf install -y python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Copy the dataset into the container
COPY ./dataset.csv /home/doc-bd-a1/dataset.csv

# Start bash shell upon container startup
CMD ["/bin/bash"]
```

---

### 2. **Docker Project Setup**

#### **Step 1: Create a Directory (`bd-a1/`) and Download Dataset**
- **Create the directory**: 
  ```bash
  mkdir bd-a1
  cd bd-a1
  ```
- **Download a dataset**: Download any simple dataset (e.g., CSV file) and place it in the `bd-a1/` directory.

#### **Step 2: Create the Dockerfile**
The `Dockerfile` defines how to build the Docker image. It specifies:
- The base image (`Ubuntu` or `Fedora`).
- Installation of required packages (Python and necessary libraries).
- Creation of a directory inside the container.
- Copying the dataset to the container.

**Dockerfile Example** (provided above).

#### **Step 3: Build the Docker Image**
To build the Docker image from the `Dockerfile`:
```bash
docker build -t my-python-image .
```

#### **Step 4: Run the Container**
Once the image is built, you can run the container:
```bash
docker run -it --name my-python-container my-python-image
```

#### **Step 5: Create Python and Bash Files**
Inside the running container:
1. **Create `load.py`**: This script will read the dataset dynamically using the provided file path argument.
    ```python
    import pandas as pd
    import sys

    def load_dataset(file_path):
        df = pd.read_csv(file_path)
        return df

    if __name__ == "__main__":
        dataset_path = sys.argv[1]
        df = load_dataset(dataset_path)
        print(df.head())
    ```

2. **Create `dpre.py`**: This file will handle data cleaning, transformation, reduction, and discretization.
    ```python
    import pandas as pd

    def data_cleaning(df):
        df = df.dropna()  # Remove missing values
        return df

    def data_transformation(df):
        df['column'] = df['column'].apply(lambda x: x * 2)  # Example transformation
        return df

    def data_reduction(df):
        df = df[['column1', 'column2']]  # Selecting relevant columns
        return df

    def data_discretization(df):
        df['column'] = pd.cut(df['column'], bins=3, labels=["Low", "Medium", "High"])  # Discretization
        return df

    def main(file_path):
        df = pd.read_csv(file_path)
        df = data_cleaning(df)
        df = data_transformation(df)
        df = data_reduction(df)
        df = data_discretization(df)
        df.to_csv('res_dpre.csv', index=False)

    if __name__ == "__main__":
        file_path = 'dataset.csv'  # Use the path to your dataset
        main(file_path)
    ```

3. **Create `eda.py`**: Perform exploratory data analysis.
    ```python
    import pandas as pd

    def perform_eda(df):
        insights = []
        insights.append(f"Mean of column1: {df['column1'].mean()}")
        insights.append(f"Std dev of column2: {df['column2'].std()}")
        insights.append(f"Correlation between column1 and column2: {df['column1'].corr(df['column2'])}")
        return insights

    def main(file_path):
        df = pd.read_csv(file_path)
        insights = perform_eda(df)
        with open('eda-in-1.txt', 'w') as f:
            for insight in insights:
                f.write(f"{insight}\n")

    if __name__ == "__main__":
        file_path = 'dataset.csv'
        main(file_path)
    ```

4. **Create `vis.py`**: Generate a simple visualization.
    ```python
    import pandas as pd
    import matplotlib.pyplot as plt

    def create_visualization(df):
        df['column1'].plot(kind='hist')
        plt.savefig('vis.png')

    def main(file_path):
        df = pd.read_csv(file_path)
        create_visualization(df)

    if __name__ == "__main__":
        file_path = 'dataset.csv'
        main(file_path)
    ```

5. **Create `model.py`**: Implement K-means clustering.
    ```python
    import pandas as pd
    from sklearn.cluster import KMeans

    def apply_kmeans(df):
        kmeans = KMeans(n_clusters=3, random_state=42)
        df['Cluster'] = kmeans.fit_predict(df[['column1', 'column2']])
        return df

    def main(file_path):
        df = pd.read_csv(file_path)
        df = apply_kmeans(df)
        df['Cluster'].value_counts().to_csv('k.txt', header=False)

    if __name__ == "__main__":
        file_path = 'dataset.csv'
        main(file_path)
    ```

6. **Create `final.sh`**: A bash script to copy the results back to the local machine.
    ```bash
    #!/bin/bash
    docker cp my-python-container:/home/doc-bd-a1/res_dpre.csv /path/to/local/bd-a1/service-result/
    docker cp my-python-container:/home/doc-bd-a1/eda-in-1.txt /path/to/local/bd-a1/service-result/
    docker cp my-python-container:/home/doc-bd-a1/vis.png /path/to/local/bd-a1/service-result/
    docker cp my-python-container:/home/doc-bd-a1/k.txt /path/to/local/bd-a1/service-result/
    docker stop my-python-container
    ```

#### **Step 6: Execute the Pipeline**
To run the pipeline inside the container:
```bash
python3 load.py /home/doc-bd-a1/dataset.csv
python3 dpre.py /home/doc-bd-a1/dataset.csv
python3 eda.py /home/doc-bd-a1/dataset.csv
python3 vis.py /home/doc-bd-a1/dataset.csv
python3 model.py /home/doc-bd-a1/dataset.csv
```

#### **Step 7: Copy Results to Local Machine**
Run the `final.sh` script to copy the results back:
```bash
bash final.sh
```

### Conclusion:
This report outlines the Docker commands required for the setup and execution of a data analysis pipeline using Docker. It covers the essential steps, from creating the Dockerfile to setting up Python scripts for data preprocessing, exploratory analysis, visualization, and machine learning. The bash script is used to copy the generated results back to the local machine.

Let me know if you need further clarification or assistance!
