using UnityEngine;
using UnityEngine.EventSystems;

public class CameraController : MonoBehaviour, IPointerUpHandler, IPointerDownHandler
{
    [SerializeField] private Transform rotator;
    [SerializeField] private Transform rotationPoint;
    [SerializeField] private float sensitivity;
    [SerializeField] private Vector2 minMaxFov;
    [SerializeField] private float zoomSensitivity;

    private Vector3 mouseReference;
    private Vector3 mouseOffset;
    private float rotation;
    private bool isRotating;

    private void Start()
    {
        rotator.LookAt(rotationPoint);
        rotation = 0;
        isRotating = false;
    }

    private void Update()
    {
        float fov = Camera.main.fieldOfView;
        fov += Input.GetAxis("Mouse ScrollWheel") * zoomSensitivity;
        fov = Mathf.Clamp(fov, minMaxFov.x, minMaxFov.y);
        Camera.main.fieldOfView = fov;

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