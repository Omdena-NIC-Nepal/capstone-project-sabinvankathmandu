from scripts.climate.models import *

import sys
import streamlit as st
import matplotlib.pyplot as plt

sys.path.append(
    "C:/My Computer/D DRIVE/Omdena/assignment/capstoneproject/capstone-project-sabinvankathmandu"
)


def show(df):
    st.title("Train & Evaluate Climate Regression Models")

    # Prepare features
    X, y = prepare_features(df)

    # Test size slider
    test_size = st.slider("Select Test Size", 0.1, 0.99, 0.2)

    # Split data
    X_train, X_test, y_train, y_test = split_data(X, y, test_size)

    # Show sizes
    st.write(f"**Training Data Size:** {len(X_train)}")
    st.write(f"**Test Data Size:** {len(X_test)}")

    # Select model type
    model_type = st.selectbox(
        "Select Model Type",
        ["Random Forest", "Ridge", "Lasso", "Gradient Boosting"]
    )

    # Train model button
    if st.button("Train Model"):
        with st.spinner("Training the model..."):
            model = train_model(X_train, y_train, model_type)
            metrics = evaluate_model(model, X_train, y_train, X_test, y_test)

            # Metrics display
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Training Metrics")
                st.metric("RMSE", f"{metrics['train_rmse']:.2f} C")
                st.metric("R²", f"{metrics['train_r2']:.4f}")
                st.metric("MAE", f"{metrics['train_mae']:.2f} C")

            with col2:
                st.subheader("Testing Metrics")
                st.metric("RMSE", f"{metrics['test_rmse']:.2f} C")
                st.metric("R²", f"{metrics['test_r2']:.4f}")
                st.metric("MAE", f"{metrics['test_mae']:.2f} C")

            # Save model
            save_model(model)
            st.success("✅ Model Trained and Saved Successfully!")
            st.session_state["model"] = model

            # Plot predictions
            st.subheader("📈 Actual vs Predicted (Test Data)")
            fig, ax = plt.subplots()
            ax.scatter(metrics["y_test"], metrics["y_pred_test"], color="blue", label="Predicted")
            ax.plot(
                [metrics["y_test"].min(), metrics["y_test"].max()],
                [metrics["y_test"].min(), metrics["y_test"].max()],
                color="red",
                linestyle="--",
                label="Perfect Prediction"
            )
            ax.set_xlabel("Actual")
            ax.set_ylabel("Predicted")
            ax.set_title("Actual vs Predicted Temperature")
            ax.legend()
            st.pyplot(fig)
