using UnityEngine;

public class CameraController : MonoBehaviour
{
    [SerializeField] private Transform rotationPoint;
    [SerializeField] private float sensitivity;

    private Vector3 mouseReference;
    private Vector3 mouseOffset;
    private float rotation;
    private bool isRotating;

    private void Start()
    {
        rotation = 0;
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            isRotating = true;
            mouseReference = Input.mousePosition;
            rotation = 0;
        }

        if (Input.GetKeyUp(KeyCode.Mouse0))
        {
            isRotating = false;
        }

        if (isRotating)
        {
            // offset
            mouseOffset = (Input.mousePosition - mouseReference);

            // apply rotation
            rotation = -(mouseOffset.x + mouseOffset.y) * sensitivity;

            // rotate
            transform.RotateAround(rotationPoint.position, Vector3.up, rotation);

            // store mouse
            mouseReference = Input.mousePosition;
        }
    }
}