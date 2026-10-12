# ML CI/CD Assignment

A small scikit-learn Decision Tree classifier trained on the Iris dataset, tested with pytest, and deployed to GitHub Pages through GitHub Actions.

## Files
- `model.py` — trains the model, predicts a sample, and prints accuracy.
- `test_model.py` — automated pytest tests.
- `requirements.txt` — Python dependencies.
- `.github/workflows/cicd.yml` — CI followed by CD (`needs: ci`).
- `index.html` — GitHub Pages project page.

## GitHub setup
1. Create a **Public** repository named `ML-CICD-Assignment`, with `main` as the default branch.
2. Upload the project files to the repository root. Ensure the hidden `.github/workflows/cicd.yml` file is included.
3. Open **Settings → Pages** and choose **GitHub Actions** as the build and deployment source if prompted.
4. Open **Actions** and wait for the `ML CI-CD Pipeline` workflow to finish. CI runs first; deployment runs only after CI passes on `main`.
5. Once the deploy job succeeds, open **Settings → Pages** to find the website URL.

The provided workflow deploys the `index.html` file from the `public` directory created during the workflow.
