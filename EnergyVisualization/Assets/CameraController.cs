using UnityEngine;
using UnityEngine.EventSystems;

public class CameraController : MonoBehaviour, IPointerUpHandler, IPointerDownHandler
{
    [SerializeField] private Transform rotator;
    [SerializeField] private Transform rotationPoint;
    [SerializeField] private float sensitivity;

    private Vector3 mouseReference;
    private Vector3 mouseOffset;
    private float rotation;
    private bool isRotating;

    private void Start()
    {
        rotation = 0;
        isRotating = false;
    }

    private void Update()
    {
        if (isRotating)
        {
            // offset
            mouseOffset = (Input.mousePosition - mouseReference);

            // apply rotation
            rotation = -(mouseOffset.x + mouseOffset.y) * sensitivity;

            // rotate
            rotator.RotateAround(rotationPoint.position, Vector3.up, rotation);

            // store mouse
            mouseReference = Input.mousePosition;
        }
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        mouseReference = Input.mousePosition;
        isRotating = true;
        rotation = 0;
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        isRotating = false;
    }
}